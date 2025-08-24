import matplotlib.pyplot as plt


def decorate_axes(ax, x, y, title, text_coords, annotate_coords):
    """
    Функция добавляет линии, заголовок, подписи, текст и аннотацию на переданный Axes.

    ax : matplotlib.axes.Axes — объект оси
    x, y : list — данные для построения линии
    title : str — заголовок графика
    text_coords : tuple (x_text, y_text, text_str) — координаты и текст для ax.text
    annotate_coords : tuple (text, xy, xytext) — параметры для ax.annotate
    """
    ax.plot(x, y, marker='o')  # строим линию
    ax.set_title(title)  # заголовок
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    # Добавляем текст
    x_text, y_text, txt = text_coords
    ax.text(x_text, y_text, txt)

    # Добавляем аннотацию с стрелкой
    ann_text, xy, xytext = annotate_coords
    ax.annotate(ann_text, xy=xy, xytext=xytext, arrowprops=dict(facecolor='black', shrink=0.05))


# --- Пример использования ---

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

decorate_axes(
    ax1,
    x=[200, 201, 202, 203, 204, 205],
    y=[31.44, 29.86, 29.60, 25.63, 25.49, 25.58],
    title="График 1",
    text_coords=(201, 29, "text 1"),
    annotate_coords=("annotate", (202, 29.6), (204, 30))
)

decorate_axes(
    ax2,
    x=[200, 201, 202, 203, 204, 205],
    y=[25, 26, 27, 28, 29, 30],
    title="График 2",
    text_coords=(202, 27, "text 2"),
    annotate_coords=("annotate 2", (203, 28), (204, 29))
)

plt.show()
