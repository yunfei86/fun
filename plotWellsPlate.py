import matplotlib.pyplot as plt
import sys, os

def main(output="."):
    xLen=12
    yLen=8
    size = 1400
    bubbleColor = "#FFFFFF"
    axisSize = 25

    # create data
    coordinates=[(x,y) for x in range(1,xLen+1) for y in range(1,yLen+1)]
    x, y = zip(*coordinates)
    sizes, colors =[size]*(xLen*yLen), [bubbleColor]*(xLen*yLen)

    # set up canvas
    fig, ax = plt.subplots(1,1, figsize=(10, 6), edgecolor="#FFFFFF", facecolor="#FFFFFF", dpi=100)

    # plot bubble plot
    ax.scatter(x, y, s=sizes, marker='o', c=colors)

    # set tick labels
    ax.xaxis.tick_top()
    plt.xticks(range(1,xLen+1), range(1,xLen+1), fontsize= axisSize  )
    plt.yticks(range(1,yLen+1), [chr(65 + x) for x in xrange(yLen)][::-1],fontsize= axisSize)
    plt.subplots_adjust(bottom = 0.1, left = 0.15)
    plt.margins(0.1)

    # remove spines
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')

    # remove ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # test
    #plt.show()

    plt.savefig(os.path.join(output,'96wellsPlate.png'))

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Usage: python sys.argv[0] <output path>"
        exit()

    main(sys.argv[1])