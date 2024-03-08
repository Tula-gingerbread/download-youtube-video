#!/usr/bin/env python3

import os
import subprocess
import string

try:
    from pytube import YouTube
except ModuleNotFoundError:
    print('Pytube not found!')
    exit(2)


def download(link: str, download_to: str|None=None, convert_to_mp3: bool=False) -> bool:
    if download_to:
        os.chdir(download_to)

    video = YouTube(link)

    filename = ''.join([char  for char in video.title  if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '])

    try:
        video.streams.get_highest_resolution().download(filename=filename)
    except Exception as ex:
        print(f'Error! {ex}')
        return False
    else:
        print('Download success.')
    
    if convert_to_mp3:
        out_filename = filename + '.mp3'

        exit_code = subprocess.call(['ffmpeg', '-i', filename + mp4, '-vn', '-acodec', 'libmp3lame', '-ab', '256k', out_filename])
        return True, exit_code

    return True



def main():
    save_to = input('Save to (empty to current directory): ')
    link = input('Link: ')
    convert_to_mp3 = input('Also convert video to mp3? [Y]es/[N]o ')
    
    convert_to_mp3 = convert_to_mp3.strip().lower() in ['y', 'yes']

    download(link.strip(), save_to.strip(), convert_to_mp3)

if __name__ == '__main__':
    main()

