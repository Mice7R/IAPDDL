;/* vim: set ff=unix ts=4 sw=4 tw=0 sts=4 et :*/
(define (problem test-01) (:domain planificador)
    (:objects l1 l2 l3 b4 b5 - libro)
    (:init
        (predecesor l1 l2)
        (predecesor l2 l3)
        (predecesor b4 b5)

        (leer l3)
        (leer b5)
    )

    (:goal (forall (?x - libro) (not (leer ?x)))))

