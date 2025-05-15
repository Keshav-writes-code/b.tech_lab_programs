(defparameter *jug-a-capacity* 4)
(defparameter *jug-b-capacity* 3)
(defparameter *goal* 2)

(defun state-equal (s1 s2)
  (and (= (first s1) (first s2))
       (= (second s1) (second s2))))

(defun goal-state-p (state)
  (= (first state) *goal*))

(defun move (state)
  (let ((a (first state))
        (b (second state)))
    ;; Generate all possible next states
    (remove-duplicates
     (list
      ;; Fill Jug A
      (list *jug-a-capacity* b)
      ;; Fill Jug B
      (list a *jug-b-capacity*)
      ;; Empty Jug A
      (list 0 b)
      ;; Empty Jug B
      (list a 0)
      ;; Pour A -> B
      (let* ((total (+ a b))
             (new-b (min *jug-b-capacity* total))
             (new-a (- total new-b)))
        (list new-a new-b))
      ;; Pour B -> A
      (let* ((total (+ a b))
             (new-a (min *jug-a-capacity* total))
             (new-b (- total new-a)))
        (list new-a new-b)))
     :test #'state-equal)))

(defun bfs ()
  (let ((queue (list (list '(0 0))))
        (visited '()))
    (loop while queue do
         (let* ((path (first queue))
                (state (first path)))
           (setf queue (rest queue))
           (unless (member state visited :test #'state-equal)
             (push state visited)
             (when (goal-state-p state)
               (return (reverse path)))
             (dolist (next (move state))
               (push (cons next path) queue))))))
  )

(defun solve-water-jug ()
  (let ((solution (bfs)))
    (if solution
        (progn
          (format t "Solution found:~%")
          (dolist (state solution)
            (format t "Jug A: ~A, Jug B: ~A~%" (first state) (second state))))
        (format t "No solution found.~%")))

;; Run the solver
(solve-water-jug)
