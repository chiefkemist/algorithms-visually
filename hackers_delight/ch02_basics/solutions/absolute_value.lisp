;;;; Hacker's Delight Section 2-4: Absolute Value Function — Solutions

(defun to-i32 (x)
  "Convert to signed 32-bit integer."
  (let ((val (logand x #xFFFFFFFF)))
    (if (>= val #x80000000)
        (- val #x100000000)
        val)))

(defun branchless-abs (x)
  "y = x >> 31; (x ^ y) - y"
  (let* ((x (to-i32 x))
         (y (ash x -31)))
    (to-i32 (- (logxor x y) y))))

(defun branchless-nabs (x)
  "y = x >> 31; y - (x ^ y)"
  (let* ((x (to-i32 x))
         (y (ash x -31)))
    (to-i32 (- y (logxor x y)))))

;;; Tests
(defun run-tests ()
  (assert (= (branchless-abs 0) 0))
  (assert (= (branchless-abs 1) 1))
  (assert (= (branchless-abs -1) 1))
  (assert (= (branchless-abs 42) 42))
  (assert (= (branchless-abs -42) 42))
  (assert (= (branchless-abs 2147483647) 2147483647))
  (assert (= (branchless-abs -2147483647) 2147483647))

  (assert (= (branchless-nabs 0) 0))
  (assert (= (branchless-nabs 1) -1))
  (assert (= (branchless-nabs -1) -1))
  (assert (= (branchless-nabs 42) -42))
  (assert (= (branchless-nabs -42) -42))
  (assert (= (branchless-nabs 2147483647) -2147483647))
  (assert (= (branchless-nabs -2147483647) -2147483647))
  (assert (= (branchless-nabs -2147483648) -2147483648))

  (format t "All absolute_value tests passed!~%"))

(run-tests)
