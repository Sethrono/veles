"""
Created on Feb 11, 2014

Mapping between numpy and opencl types

Copyright (c) 2013 Samsung Electronics Co., Ltd.
"""

import numpy

import veles.error as error


# : CL type defines
cl_defines = {"float":      {"dtype": "float",
                             "sizeof_dtype": "4"},
              "double":     {"dtype": "double",
                             "sizeof_dtype": "8"}}


# : Supported types as OpenCL => numpy dictionary.
dtypes = {"float": numpy.float32, "double": numpy.float64}


# : Map between numpy types and opencl.
def numpy_dtype_to_opencl(dtype):
    if dtype == numpy.float32:
        return "float"
    if dtype == numpy.float64:
        return "double"
    if dtype == numpy.complex64:
        return "float2"
    if dtype == numpy.complex128:
        return "double2"
    if dtype == numpy.int8:
        return "char"
    if dtype == numpy.int16:
        return "short"
    if dtype == numpy.int32:
        return "int"
    if dtype == numpy.int64:
        return "long"
    if dtype == numpy.uint8:
        return "uchar"
    if dtype == numpy.uint16:
        return "ushort"
    if dtype == numpy.uint32:
        return "uint"
    if dtype == numpy.uint64:
        return "ulong"
    raise error.NotExistsError()
