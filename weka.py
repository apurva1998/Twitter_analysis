from weka.experiments import SimpleCrossValidationExperiment, SimpleRandomSplitExperiment, Tester, ResultMatrix
from weka.classifiers import Classifier
import weka.core.converters as converters
# configure experiment
datasets = ["bolts.arff", "bodyfat.arff"]
classifiers = [Classifier(classname="weka.classifiers.rules.ZeroR"), Classifier(classname="weka.classifiers.functions.LinearRegression")]
outfile = "results-rs.arff"   # store results for later analysis
exp = SimpleRandomSplitExperiment(
    classification=False,
    runs=10,
    percentage=66.6,
    preserve_order=False,
    datasets=datasets,
    classifiers=classifiers,
    result=outfile)
exp.setup()
exp.run()
# evaluate previous run
loader = converters.loader_for_file(outfile)
data   = loader.load_file(outfile)
matrix = ResultMatrix(classname="weka.experiment.ResultMatrixPlainText")
tester = Tester(classname="weka.experiment.PairedCorrectedTTester")
tester.resultmatrix = matrix
comparison_col = data.attribute_by_name("Correlation_coefficient").index
tester.instances = data
print(tester.header(comparison_col))
print(tester.multi_resultset_full(0, comparison_col))