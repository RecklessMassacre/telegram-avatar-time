from telethon import TelegramClient
from config import *
from utils import time_has_changed, generate_time_image_bytes
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime, timedelta
from time import sleep


client = TelegramClient(
    session='sweety', api_id=api_id, api_hash=api_hash, device_model=device_model,
    system_version=system_version, app_version=app_version, lang_code=lang_code,
    system_lang_code=system_lang_code
)


async def main():
    prev_update_time = datetime.now() - timedelta(minutes=1)

    img_bts = generate_time_image_bytes(prev_update_time)
    file = await client.upload_file(img_bts)
    await client(UploadProfilePhotoRequest(file=file))

    while True:
        if time_has_changed(prev_update_time):
            profile_photos = await client.get_profile_photos('me')
            curr_photo = [profile_photos[0], ]
            await client(DeletePhotosRequest(curr_photo))

            t = datetime.now()
            img_bts = generate_time_image_bytes(t)
            file = await client.upload_file(img_bts)
            await client(UploadProfilePhotoRequest(file=file))

            prev_update_time = datetime.now()

        sleep(1)


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
