import Rhino.Geometry as rg
import ghpythonlib.treehelpers as th 
import math

#Debugging Assignment1 

pointList1 = []
a = pointList1
pointList2 = []
b = pointList2
lineList = []
c = lineList
curvesList = []
allDivPts = []
allMovedPts = []

for i in range(count):
    pt = rg.Point3d(i,0,0) 
    pointList1.append(pt)

for j in range(count):
    pt2 = rg.Point3d(j,y,0) 
    pointList2.append(pt2)

for k in range(len(a)):
    ln = rg.Line(a[k],b[k])
    lineList.append(ln)

for line in lineList:
    linePts = []
    nc = rg.Line.ToNurbsCurve(line)
    params = rg.Curve.DivideByCount(nc,10,True)
    for p in params:
        divPt = rg.Curve.PointAt(nc,p)
        linePts.append(divPt)
    allDivPts.append(linePts)
    
d = th.list_to_tree(allDivPts)

for list in allDivPts:
    movedPts = []
    for l in list:
        vector = rg.Vector3d(l)
        vLenght = vector.Length
        mDisplacement = math.sin(vLenght)
        nVector = rg.Vector3d(0,0,mDisplacement)
        newPt = l - nVector
        movedPts.append(newPt)
    allMovedPts.append(movedPts)

d = th.list_to_tree(allMovedPts)

for list in allMovedPts:
    curve = rg.Curve.CreateInterpolatedCurve(list,3)
    curvesList.append(curve)

e = curvesList

surface = rg.Brep.CreateFromLoft(e,rg.Point3d.Unset,rg.Point3d.Unset,rg.LoftType.Normal,False)
f = surface

bigMesh = rg.Mesh()
meshList = []

for i in range(len(allMovedPts)-1):
    for j in range(len(allMovedPts[i])-1):
        m = rg.Mesh()
        v0 = allMovedPts[i][j]
        v1 = allMovedPts[i][j+1]
        v2 = allMovedPts[i+1][j+1]
        v3 = allMovedPts[i+1][j]

        m.Vertices.Add(v0)
        m.Vertices.Add(v1)
        m.Vertices.Add(v2)
        m.Vertices.Add(v3)

        m.Faces.AddFace(0,1,2,3)

        bigMesh.Append(m)

bigMesh.Normals.ComputeNormals()
bigMesh.Weld(3.14)

g = bigMesh



