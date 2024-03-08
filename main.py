#!/usr/bin/env python3

import os

try:
    from pytube import YouTube
except ModuleNotFoundError:
    print('Pytube not found!')
    exit(2)


def download(link: str, download_to: str|None=None) -> bool:
    if download_to:
        os.chdir(download_to)

    video = YouTube(link).streams.get_highest_resolution()

    try:
        video.download()
    except Exception as ex:
        print(f'Error! {ex}')
        return False
    else:
        print('Download success.')
        return True


def main():
    save_to = input('Save to (empty to current directory): ')
    link = input('Link: ')
    
    download(link.strip(), save_to.strip())

if __name__ == '__main__':
    main()

