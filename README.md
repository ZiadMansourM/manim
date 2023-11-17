# Welcome to Visualizations Scripts of CMPS446

```console
$ docker compose up --build -d
$ docker compose ps
$ docker compose exec manim bash
```

While developing, use the following command to render the video:
```console
$ manim -qm project/hough_transform.py Main
```

For final video rendering, use the following command:
```console
$ manim -qh -r 3840,2160 project/hough_transform.py Main
```