from pycocotools.coco import COCO


dataDir = './data/coco'
dataType = 'val2017'
annFile = '{}/annotations/instances_{}.json'.format(dataDir, dataType)

coco = COCO(annFile)

## Classes
classes = coco.loadCats(coco.getCatIds())
print(classes.keys())


