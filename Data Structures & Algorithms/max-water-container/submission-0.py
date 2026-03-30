class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        min_height=0
        max_area=0
        area=0
        diff=0
        while l<r:
          

            diff=r-l
            min_height=min(heights[l],heights[r])
            area=diff*min_height
            max_area=max(area,max_area)


            if heights[l]<=heights[r]:
                l+=1
            else:

                r-=1

        return max_area


            

        