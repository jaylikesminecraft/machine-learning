def gradientDescent(data, iterations, learningRate, bterms):
    
    b0 = bterms[0]
    b1 = bterms[1]
    db0 = 0
    db1 = 0
    
    for i in range(iterations):
        
        for j in range(len(data)):
            db0 += (data[j][1] - b0 - b1*data[j][0])
        db0 = (-2) * (db0/len(data))

        b0 = b0 - learningRate * db0

        for j in range(len(data)):
            db1 += (data[j][1] - b0 - b1*data[j][0])*(data[j][0])
        db1 = (-2) * (db1/len(data))

        b1 = b1 - learningRate * db1

    return [b0, b1]
    
data = [[1,14],[3,24],[2,18],[1,17],[3,27]]
#data = [[1,3],[2,5],[3,7],[4,6],[5,9],[6,10],[7,23],[8,31],[9,21],[10,29]]
bterms = [0,0]
learning_rate = 0.01
iterations = 10000

print(gradientDescent(data, iterations, learning_rate,bterms))
