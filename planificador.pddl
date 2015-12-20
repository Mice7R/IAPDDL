;;/* vim: set ff=unix ts=4 sw=4 tw=0 sts=4 et :*/
(define (domain planificador)
    (:requirements :adl :typing)
    (:types libro - item)
    (:predicates
        (predecesor ?x - libro ?y - libro)  ;;x precede a y
        (leido ?x - libro)                  ;; ya esta leido
        (leer ?x - libro))                  ;; se tiene que leer

    (:action leer_predecesor :parameters (?x - libro ?y - libro)
        :precondition (and (predecesor ?x ?y) (not (leer ?x)))
        :effect (leer ?x))

    (:action leer_libro :parameters (?x - libro)
        :precondition (and (leer ?x) (forall (?y - libro) (or (not (predecesor ?y ?x)) (leido ?y))))
        :effect (and (not (leer ?x)) (leido ?x)))

)
