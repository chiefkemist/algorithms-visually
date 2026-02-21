;;;; Hacker's Delight Section 2-1: Manipulating Rightmost Bits — Solutions

(defun mask32 (x)
  "Mask to 32-bit unsigned."
  (logand x #xFFFFFFFF))

(defun turn-off-lowest-bit (x)
  "x & (x - 1)"
  (mask32 (logand x (1- x))))

(defun turn-on-lowest-zero-bit (x)
  "x | (x + 1)"
  (mask32 (logior x (1+ x))))

(defun isolate-lowest-bit (x)
  "x & (-x)"
  (mask32 (logand x (- x))))

(defun isolate-lowest-zero-bit (x)
  "~x & (x + 1)"
  (mask32 (logand (lognot x) (1+ x))))

(defun mask-from-lowest-bit (x)
  "x ^ (x - 1)"
  (mask32 (logxor x (1- x))))

(defun turn-off-trailing-ones (x)
  "x & (x + 1)"
  (mask32 (logand x (1+ x))))

(defun turn-on-trailing-zeros (x)
  "x | (x - 1)"
  (mask32 (logior x (1- x))))

(defun power-of-two-p (x)
  "x != 0 and x & (x - 1) == 0"
  (and (/= x 0) (zerop (logand x (1- x)))))

;;; Tests
(defun run-tests ()
  ;; turnOffLowestBit
  (assert (= (turn-off-lowest-bit #b01011000) #b01010000))
  (assert (= (turn-off-lowest-bit #b01010100) #b01010000))
  (assert (= (turn-off-lowest-bit #b00000001) 0))
  (assert (= (turn-off-lowest-bit #x80000000) 0))
  (assert (= (turn-off-lowest-bit #b11111111) #b11111110))
  (assert (= (turn-off-lowest-bit 0) 0))

  ;; turnOnLowestZeroBit
  (assert (= (turn-on-lowest-zero-bit #b10100111) #b10101111))
  (assert (= (turn-on-lowest-zero-bit #b01010100) #b01010101))
  (assert (= (turn-on-lowest-zero-bit 0) 1))
  (assert (= (turn-on-lowest-zero-bit #b01111111) #b11111111))
  (assert (= (turn-on-lowest-zero-bit #x7FFFFFFF) #xFFFFFFFF))

  ;; isolateLowestBit
  (assert (= (isolate-lowest-bit #b01011000) #b00001000))
  (assert (= (isolate-lowest-bit #b01010100) #b00000100))
  (assert (= (isolate-lowest-bit #b11111111) 1))
  (assert (= (isolate-lowest-bit 0) 0))
  (assert (= (isolate-lowest-bit 64) 64))
  (assert (= (isolate-lowest-bit #b10101010) 2))

  ;; isolateLowestZeroBit
  (assert (= (isolate-lowest-zero-bit #b10100111) #b00001000))
  (assert (= (isolate-lowest-zero-bit #b11111110) 1))
  (assert (= (isolate-lowest-zero-bit 0) 1))
  (assert (= (isolate-lowest-zero-bit #b11111101) #b00000010))
  (assert (= (isolate-lowest-zero-bit #xFFFFFFFF) 0))

  ;; maskFromLowestBit
  (assert (= (mask-from-lowest-bit #b01011000) #b00001111))
  (assert (= (mask-from-lowest-bit #b01010100) #b00000111))
  (assert (= (mask-from-lowest-bit #b11111111) 1))
  (assert (= (mask-from-lowest-bit 1) 1))
  (assert (= (mask-from-lowest-bit #x80000000) #xFFFFFFFF))
  (assert (= (mask-from-lowest-bit 0) #xFFFFFFFF))

  ;; turnOffTrailingOnes
  (assert (= (turn-off-trailing-ones #b10100111) #b10100000))
  (assert (= (turn-off-trailing-ones #b11111111) 0))
  (assert (= (turn-off-trailing-ones #b10101000) #b10101000))
  (assert (= (turn-off-trailing-ones 0) 0))
  (assert (= (turn-off-trailing-ones #xFFFFFFFF) 0))

  ;; turnOnTrailingZeros
  (assert (= (turn-on-trailing-zeros #b10101000) #b10101111))
  (assert (= (turn-on-trailing-zeros #b01010111) #b01010111))
  (assert (= (turn-on-trailing-zeros 0) #xFFFFFFFF))
  (assert (= (turn-on-trailing-zeros #b11111111) #b11111111))
  (assert (= (turn-on-trailing-zeros #x80000000) #xFFFFFFFF))

  ;; isPowerOfTwo
  (assert (not (power-of-two-p 0)))
  (assert (power-of-two-p 1))
  (assert (power-of-two-p 2))
  (assert (power-of-two-p 4))
  (assert (power-of-two-p 1024))
  (assert (power-of-two-p #x80000000))
  (assert (not (power-of-two-p 3)))
  (assert (not (power-of-two-p 6)))
  (assert (not (power-of-two-p 255)))
  (assert (not (power-of-two-p #xFFFFFFFF)))

  (format t "All rightmost_bits tests passed!~%"))

(run-tests)
