```console
$ docker compose up --build -d
$ docker compose ps
$ docker compose exec manim bash
```

```console
$ manim -qm square-to-circle/main.py CircleToSquare
$ manim -qm project/hough.py HoughTransformScene
```

```
$ manim -qm project/hough_transform.py Main
$ manim -qh -r 3840,2160 project/hough_transform.py Main
```