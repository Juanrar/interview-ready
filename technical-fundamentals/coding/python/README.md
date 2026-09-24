# Coding challenges en Python

Versión en Python de los ejercicios de `technical-fundamentals/coding`.

Cada archivo tiene el enunciado, la función o clase a implementar y sus tests al final.

## Cómo correr los tests

Requiere Python 3.10+ y pytest (`pip install pytest`).

```
cd technical-fundamentals/coding/python
pytest                                  # todos los ejercicios
pytest problems/01_is_unique.py         # un ejercicio
pytest problems/01_is_unique.py -k empty  # un test puntual
```

Los tests fallan hasta que implementes cada ejercicio.

`code_review/` no tiene tests. Es código con problemas a propósito, para practicar code review.
