from datetime import datetime
from numpy import zeros
import cv2


def convert_time_to_string(dt):
    return f"{dt.hour:02}:{dt.minute:02}"


def time_has_changed(prev_time):
    return datetime.now().replace(second=0, microsecond=0) != prev_time.replace(second=0, microsecond=0)


def get_black_background():
    return zeros((500, 500))


def generate_time_image_bytes(dt):
    text = convert_time_to_string(dt)
    image = get_black_background()

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(
        image, text, (int(image.shape[0] * 0.035), int(image.shape[1] * 0.6)),
        font, 5.2, (255, 255, 0), 17, cv2.LINE_AA
    )

    _, bts = cv2.imencode('.jpg', image)

    return bts.tobytes()
