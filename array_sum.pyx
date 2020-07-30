#cython: language_level=3

cdef extern from "array_sum_c.c":
    int arraysum(int[] inarray)
    
cpdef array_sum(inarray):
    arraysum(int[] inarray)