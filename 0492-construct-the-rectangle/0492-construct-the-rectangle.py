class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mn=float(inf)
        a =[area, 1]
        for width in range(1, int(area**0.5)+1):
            length=area/width
            if(length==int(length) and length>=width and length-width<mn):
                a[0]=int(length)
                a[1]=width
                mn=length-width
        return a
        