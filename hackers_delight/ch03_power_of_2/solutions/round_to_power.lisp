;;;; Hacker's Delight Section 3-2: Rounding to Powers of 2 — Solutions

(defun mask32 (x)
  (logand x #xFFFFFFFF))

(defun round-up-to-pow2 (x)
  "clp2: round up to next power of 2."
  (if (= x 0) (return-from round-up-to-pow2 0))
  (let ((v (mask32 (1- x))))
    (setf v (logior v (ash v -1)))
    (setf v (logior v (ash v -2)))
    (setf v (logior v (ash v -4)))
    (setf v (logior v (ash v -8)))
    (setf v (logior v (ash v -16)))
    (mask32 (1+ v))))

(defun round-down-to-pow2 (x)
  "flp2: round down to previous power of 2."
  (let ((v x))
    (setf v (logior v (ash v -1)))
    (setf v (logior v (ash v -2)))
    (setf v (logior v (ash v -4)))
    (setf v (logior v (ash v -8)))
    (setf v (logior v (ash v -16)))
    (- v (ash v -1))))

(defun floor-log2 (x)
  "Floor of log base 2."
  (assert (> x 0))
  (let ((n 0) (v x))
    (when (>= v (ash 1 16)) (incf n 16) (setf v (ash v -16)))
    (when (>= v (ash 1 8))  (incf n 8)  (setf v (ash v -8)))
    (when (>= v (ash 1 4))  (incf n 4)  (setf v (ash v -4)))
    (when (>= v (ash 1 2))  (incf n 2)  (setf v (ash v -2)))
    (when (>= v (ash 1 1))  (incf n 1))
    n))

;;; Tests
(defun run-tests ()
  (assert (= (round-up-to-pow2 0) 0))
  (assert (= (round-up-to-pow2 1) 1))
  (assert (= (round-up-to-pow2 2) 2))
  (assert (= (round-up-to-pow2 3) 4))
  (assert (= (round-up-to-pow2 5) 8))
  (assert (= (round-up-to-pow2 8) 8))
  (assert (= (round-up-to-pow2 9) 16))
  (assert (= (round-up-to-pow2 13) 16))
  (assert (= (round-up-to-pow2 200) 256))
  (assert (= (round-up-to-pow2 #x80000000) #x80000000))

  (assert (= (round-down-to-pow2 0) 0))
  (assert (= (round-down-to-pow2 1) 1))
  (assert (= (round-down-to-pow2 2) 2))
  (assert (= (round-down-to-pow2 3) 2))
  (assert (= (round-down-to-pow2 5) 4))
  (assert (= (round-down-to-pow2 8) 8))
  (assert (= (round-down-to-pow2 13) 8))
  (assert (= (round-down-to-pow2 200) 128))
  (assert (= (round-down-to-pow2 #xFFFFFFFF) #x80000000))

  (assert (= (floor-log2 1) 0))
  (assert (= (floor-log2 2) 1))
  (assert (= (floor-log2 3) 1))
  (assert (= (floor-log2 8) 3))
  (assert (= (floor-log2 15) 3))
  (assert (= (floor-log2 16) 4))
  (assert (= (floor-log2 200) 7))
  (assert (= (floor-log2 #xFFFFFFFF) 31))

  (format t "All round_to_power tests passed!~%"))

(run-tests)
