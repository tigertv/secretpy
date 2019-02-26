#!/usr/bin/python

from .abstractmachine import AbstractCryptMachine

class CompositeMachine(AbstractCryptMachine):
	__machines = []

	def __init__(self, *machines):
		for machine in machines:
			self.__machines.append(machine)

	def encrypt(self, text):
		ret = text 
		for machine in self.__machines:
			ret = machine.encrypt(ret)
		return ret

	def decrypt(self, text):
		ret = text 
		for machine in self.__machines:
			ret = machine.decrypt(ret)
		return ret
	
	def addMachine(self, *machines):
		for machine in machines:
			self.__machines.append(machine)
