#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           c0#��)C�v���iy	N:��Β_�w~m����Ŀ��)"�S#�y-;Q+�`��*
��9�$P��ww�	�'��=WnG|1	�\&gN������`J��!��8�
f����ԡ_l-��,"""
from hashlib import sha256
#print sha256(blob).hexdigest()
digest = sha256(blob).hexdigest()
if digest[0] == "7" :
	print "I come in peace."
if digest[0] == "0" :
	print "Prepare to be destroyed!"
