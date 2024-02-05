import curses #0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, and 7:white

def main(stdscr):

    debug = False
    grid_size = 10
    default_grid_icon = "X"

    curses.noecho()
    curses.curs_set(1)  
    stdscr.clear()

    
    UserRequest="NOT X"
    mode="regular"
    while UserRequest != "x":
        grid = CreateGrid(grid_size, default_grid_icon)
        PlaceGrid(stdscr, grid, True)
        stdscr.refresh()
        UserRequest = GetUserInput(stdscr)
        match(mode):                
            case "placement":
                UserRequest = UserRequest.split()
                PlaceMessage(stdscr, "Icon", 0, 1, 0, -1)


        stdscr.clear()
        if UserRequest == "p":
            mode = "placement"
            PlaceMessage(stdscr, "Placementmode", 0, 1, 0, -1)
        else:
            mode = "regular"
            PlaceMessage(stdscr, UserRequest, 0, 1)
    
    print("Exited gracefully escaping the main loop")
    
    
    
    



def PlaceMessage( stdscr ,message,location = 0, refresh=False, x_offset = 0, y_offset = 0):
    message = str(message)
    match(location):
        case 0: #middle of screen
            height, width = stdscr.getmaxyx()
            x = (width - len(message)) // 2 + x_offset
            y = height // 2 + y_offset
            stdscr.addstr(y, x, message)
        case 1: #top left of screen
            stdscr.addstr(y_offset, x_offset, message)
    if refresh:
        stdscr.refresh()
def PlaceGrid(stdscr , grid,refresh=0, x_offset = 0, y_offset =0):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            PlaceMessage(stdscr, grid[x][y],1,0, (y+x_offset), (x+y_offset))
    if refresh:
        stdscr.refresh()
def CreateGrid(grid_size, default_grid_icon):
    grid = []
    for x in range(grid_size):
        temp_grid=[]
        for y in range(grid_size):
            temp_grid.append(default_grid_icon)
        grid.append(temp_grid)
    return grid
def PlaceOnGrid(grid, x, y, icon):
    grid[y][x] = icon
    return (grid)
def GetUserInput(stdscr):
    return(stdscr.getstr()).decode("utf-8")

# Run the application
curses.wrapper(main)
