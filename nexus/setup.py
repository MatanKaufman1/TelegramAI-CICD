from setuptools import setup, find_packages

boto3_setup_args = dict(
    name='boto3',
    version='1.0.0',
    description='boto3',
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
    setup(**boto3_setup_args)


