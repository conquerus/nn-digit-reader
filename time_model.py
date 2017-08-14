import timeit

def time_it(number_of_tests):
    #Timing model fitting
    T = timeit.Timer('base_model.fit(handwriting, 0)',
                 'import _data_handler; import _model_builder; handwriting = _data_handler.Dataset(); handwriting.preproc_MLP(); base_model = _model_builder.Network(handwriting, model_type="MLP")')
    print "average execution time = "
    print T.timeit(number=number_of_tests)/number_of_tests

#the number of tests to average over
NUMBER_OF_TESTS = 3

time_it(NUMBER_OF_TESTS)
