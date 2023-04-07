# You are given an array of integers representing coordinates of obstacles situated on a straight line.

# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

# Find the minimal length of the jump enough to avoid all the obstacles.

# Example

# For inputArray = [5, 3, 6, 7, 9], the output should be
# solution(inputArray) = 4.

def solution(inputArray):
    # sort the list in ascending order
    obs = sorted(inputArray)
     
    # set jump distance to 1
    jump_dist = 1
     
    # flag to check if current jump distance
    # hits an obstacle
    obstacle_hit = True
 
    while(obstacle_hit):
         
        obstacle_hit = False
        jump_dist += 1
         
        # checking if jumping with current length
        # hits an obstacle
        for i in range(0, len(obs)):
            if obs[i] % jump_dist == 0:
                 
                # if obstacle is hit repeat process
                # after increasing jump distance
                obstacle_hit = True
                break
 
    return jump_dist
            
            

