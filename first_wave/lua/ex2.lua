
local function WhichDraw(entity, xPosition, yPosition)
    if (xPosition + yPosition) % 2 == 0 then
        io.write("*")
        return;
    end
    io.write(entity.boxSpace)

end


local function Draw(entity)
    --io.write(tonumber(entity.ySize))
    for j = 0, tonumber(entity.ySize), 1 do
        if (j==0 or j==entity.ySize) then
            for i=0, tonumber(entity.xSize), 1 do
                io.write("-")
            end
            ---io.write("\n")
            if j == entity.ySize or j==0 then
                io.write("\n")
            end
            goto continue
        end
        
        for i = 0, tonumber(entity.xSize), 1 do 
            if (i==0 or i==entity.xSize) then
                io.write(entity.verticalWall)
                
            end
            if not (i==0 or i==entity.ySize) then
                WhichDraw(entity, i, j)    
            end
            if i == entity.xSize then
                io.write("\n")
            end
            
        end
        ::continue::
        
    end
end



local function Box(xSize, ySize)
    local xSize = xSize or 10
    local ySize = ySize or 10
    

    
    return{
        xPosition=0,
        yPosition=0,
        boxSpace=' ',
        xSize = xSize,
        ySize=ySize,
        verticalWall = '|',
        horizontalWall = '-'
    }
end


io.write("Welcome to the box printer! Please introduce X and Y dimension:\n")
local xSize = tonumber(io.read())
local ySize = tonumber(io.read())
local start = os.clock()
_G.myBox = Box(xSize, ySize)
Draw(myBox)
print("\n", os.clock() - start)
