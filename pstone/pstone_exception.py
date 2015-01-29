#!/usr/bin/env python


class PStoneException(Exception):
    # ToDo - Make it better exception
    def __str__(self):
        return self.__info
