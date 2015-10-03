# coding=utf8
__author__ = 'hellflame'

from setuptools import setup, find_packages

setup(
    name='FlowCheck',
    version='0.3',
    keywords=('quantity of flow', 'flow check', 'flow'),
    description="在linux终端基于ip命令获取统计通过网卡的流量信息",
    license='MIT',
    author="hellflame",
    author_email="hellflamedly@gmail.com",
    url='https://github.com/hellflame/flow_check',
    packages=find_packages(),
    platforms='Ubuntu',
    entry_points={
        'console_scripts': [
            'flower=flow.flower:main'
        ]
    }
)

