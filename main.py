#!/usr/bin/env python3 

import os
import subprocess

try:
    from pytube import YouTube
except ModuleNotFoundError:
    print('Pytube not found!')
    exit(2)


def download(link: str, download_to: str|None=None, convert_to_mp3: bool=False,
            write_output: bool=True, check_link: bool=True) -> tuple[bool, int]:
    """
    Download youtube video.

    Required arguments:
    link: link to video

    Optional arguments:
    download_to    : path to download. if None download to current dir
    convert_to_mp3 : if True, convert downloaded video to mp3. (ffmpeg required)
    write_output   : if False, no output will be displayed
    check_link     : if False, link check will be skipped

    Return: tuple[bool, int]
    If bool is True, the download is completed successfully. int is the return of ffmpeg (if mp3 conversion is specified) or 0.
    If bool is False, then something went wrong. Int: 1 - the download directory was not found, 2 - link verification error, 3 - error during download.
    """

    def smart_print(*args, **kwargs):
        if write_output:
            print(args, kwargs)

    if download_to:
        if os.path.isdir(download_to):
            os.chdir(download_to)
        else:
            smart_print('Unknown directory!')
            return (False, 1)

    if check_link and not link.startswith(('https://www.youtube.com/', 'https://youtu.be/')):
        smart_print('YT link was expected, an unknown link was received.')
        return (False, 2)

    video = YouTube(link)

    # Filtering video name
    allowed_symbols = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789 абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ . '.replace(' ', '') + ' '
    filename = ''.join(
        [char for char in video.title if char in allowed_symbols]
    ).strip()

    try:
        video.streams.get_highest_resolution().download(filename=filename + '.mp4')
    except Exception as ex:
        smart_print(f'Error! {ex}')
        return (False, 3)
    else:
        smart_print('Download success.')

    if convert_to_mp3:
        exit_code = subprocess.call(
            ['ffmpeg', '-i', f'{filename}.mp4', '-vn', '-acodec', 'libmp3lame', '-ab', '256k', f'{filename}.mp3']
            )

        smart_print(f'ffmpeg exit code: {exit_code}')
        return (True, exit_code)

    return (True, 0)


def main():
    save_to = input('Save to (empty to current directory): ').strip()
    link = input('Link: ').strip()
    convert_to_mp3 = input('Also convert video to mp3? [Y]es/[N]o ').strip().lower() in ['y', 'yes']

    download(link, save_to, convert_to_mp3)

if __name__ == '__main__':
    main()
