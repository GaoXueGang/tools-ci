# tools-ci ��copy icon��

˵��������������Դ������icon�ߴ磬�޸ĳ�ָ�����ơ�

# ���û���

1. ��װpython����2.7.4Ϊ����

2. ��װpip

	��1�� ִ�нű� python get-pip.py

	��2�� ִ�нű� python -m pip install -U pip

3. ��װPillow

	��1�� ��������2��pip�ᰲװ��python��װ·���µ�Scripts�ļ�����

	��2�� ִ�нű� pip install Pillow �� easy_install Pillow

# ʹ��˵��

1. �����ṩ��icon��Դ�Ž�srcĿ¼�£���ʽpng��������Ҫ��

2. ������Ŀʵ������޸�copy_icon.py�е�����

	��1�� ���� IOS_DIST_PATH �� ANDROID_DIST_PATH ��iOS��android��Դ���Ŀ¼��
	
	��2�� ���� IOS_IMAGE_CONFIG �� ANDROID_IMAGE_CONFIG ��iOS��android�ߴ磬���ƣ�android����Ŀ¼��

3. ִ�нű� python copy_icon.py
