from setuptools import setup, find_packages

yt_dlp_package_setup_args = dict(
    name='yt_dlp_package',
    version='1.0.0',
    description='yt-dlp Package',
    license='MIT',
    install_requires=[
        'yt-dlp>=2023.2.17',
        'pyTelegramBotAPI',
        'boto3',
        'loguru',
    ],
    author='Matt',
    author_email='example@example.com'
)

if __name__ == '__main__':
    setup(**yt_dlp_package_setup_args)


