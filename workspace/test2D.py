import os

import SimpleITK as sitk
import six

from radiomics import featureextractor, getTestCase

dataDir = './'

imageName = os.path.join(dataDir, 'forRadiomicsTest.nrrd')
maskName = os.path.join(dataDir, 'Segmentation.seg.nrrd')

params = os.path.join(dataDir, '2D_sample.yaml')

extractor = featureextractor.RadiomicsFeatureExtractor(params)

results = extractor.execute(imageName, maskName)
for key, val in six.iteritems(results):
    print("\t%s: %s" % (key, val))
