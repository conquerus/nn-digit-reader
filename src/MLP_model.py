#create the MLP model and save it
import _data_handler
import _model_builder

#load traning data
HANDWRITING = _data_handler.Dataset()
#preprocess the data for use with an MLP network
HANDWRITING.preproc_MLP()
#compile the network
BASELINE_MODEL = _model_builder.Network(HANDWRITING, 'MLP')
#fit to traning data
BASELINE_MODEL.fit(HANDWRITING, 2)
#evaluate
BASELINE_MODEL.final_eval(HANDWRITING, 2)
#save
BASELINE_MODEL.save()
