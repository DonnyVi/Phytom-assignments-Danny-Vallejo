import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th 
import math

pointList1 = []
a = pointList1
pointList2 = []
b = pointList2
lineList = []
c = lineList


for i in range(count):
    pt = rg.Point3d(i,0,0) 
    pointList1.append(pt)

for j in range(count):
    pt2 = rg.Point3d(j,y,0) 
    pointList2.append(pt2)
    
#for i in range(len(a)):
#    print a[i]

for i in a:
    print i
for j in b:
    print j
ln = rg.Line(i,j)
lineList.append(ln)


#for i in a:
#    sp = rg.Point3d(i)
#    for j in b:
#        print j
#        ep = rg.Point3d(j)
#        ln = rg.Line(sp,ep)
#    ln = rg.LineCurve(a,b)
#   ln = rg.Line(startPoint, endPoint)
#   ln = rg.Curve.CreateInterpolatedCurve(a,3)
