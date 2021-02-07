import torch
from pandas import read_table

# Build MLP for regression
# inputs=3 (X1, X2, X3), hidden=4 (4 * 4 hidden layers), output = 1(Y)
class Mlp (torch.nn.Module):
    def __init__(self, inputs, hiddens, output):
        super(Mlp, self).__init__()
        self.hidden_1 = torch.nn.Linear(inputs, hiddens)
        self.hidden_2 = torch.nn.Linear(hiddens, hiddens)
        self.hidden_3 = torch.nn.Linear(hiddens, hiddens)
        self.hidden_4 = torch.nn.Linear(hiddens, hiddens)
        self.output = torch.nn.Linear(hiddens, output)

    def forward(self, X):
        # network forward propagation
        X = self.hidden_1(X)
        X = self.hidden_2(X)
        X = self.hidden_3(X)
        X = torch.nn.functional.relu(self.hidden_4(X))
        X = self.output(X)
        return X


if __name__=='__main__':
    train_data = torch.tensor(read_table('train_data.txt', sep='\t').values)
    train_truth = torch.tensor(read_table('train_truth.txt').values)
    test_data = torch.tensor(read_table('test_data.txt', sep='\t').values)

    # optimizer params & loss function
    mlp = Mlp(inputs=3, hiddens=4, output=1)
    optimizer = torch.optim.Adam(mlp.parameters())
    loss_function = torch.nn.MSELoss()

    # data training process
    for i in range(1001):
        prediction = mlp(train_data.float())
        loss = loss_function(prediction, train_truth.float())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # result
    Y = mlp(test_data.float())
    with open('test_predicted.txt', 'w') as file:
        file.write('y'+'\n')
        for j in Y:
            file.write(('%e' % j[0].item())+'\n')

