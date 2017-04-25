// Example program
#include <iostream>
#include <string>
#include <vector>

using namespace std;


const int m = 3;
const int n = 3;

void zero(int **M) {
    int rows[m];
    int cols[n];
    
    int r = 0;
    int c = 0;
    
    for (int i=0; i < m; i++)    
        for (int j=0; j < n; j++)
            if (M[i][j] == 0) { 
                rows[r++] = i;
                cols[c++] = j;
            }
            
    for (int i=0; i < r; i++){
        for (int j=0; j < n; j++){
            M[rows[i]][j] = 0;
        }
    }
    
    for (int i=0; i < c; i++){
        for (int j=0; j < m; j++){
            M[j][cols[i]] = 0;   
        }
    }
}

vector<vector<int>> zero_vector(vector<vector<int>> M){
    vector<int> rows;
    vector<int> cols;
    
    for (int i=0; i < M.size(); i++) {
        for (int j=0; j < M[0].size(); j++){
            if (M[i][j] == 0){
                rows.push_back(i);
                cols.push_back(j);
            }
        }
    }
    
    for (vector<int>::iterator r=rows.begin(); r != rows.end(); r++){
        for (int j=0; j < M[0].size(); j++)
            M[*r][j] = 0;
    }
    
    for (vector<int>::iterator c=cols.begin(); c != cols.end(); c++){
        for (int i=0; i < M.size(); i++)
            M[i][*c] = 0;
    }
    
    return M;
}

int main()
{
    int M_arr[m][n] = {{1,2,3},{0,4,5},{6,7,0}};
    int **M;
    
    //int m = sizeof(M_arr) / sizeof(M_arr[0]);
    //int n = sizeof(M_arr[0])/sizeof(int);
    
    M = new int*[m];
    for (int i=0; i < m; i++) {
        M[i] = new int[n];
        for (int j=0; j < n; j++)
            M[i][j] = M_arr[i][j];
    }
    
    for (int i=0; i < m; i++) {
        for (int j=0; j < n; j++)
            cout << M[i][j] << " ";
        cout << endl;
    }
    
    zero(M);
    
    cout << endl;
    for (int i=0; i < m; i++) {
        for (int j=0; j < n; j++)
            cout << M[i][j] << " ";
        cout << endl;
    }
    
    cout << endl << endl;
    
    
    vector<vector<int>> N(m,vector<int> (n,0));
    
    for (int i=0; i<m; i++)
        for (int j=0; j<n; j++)
            N[i][j] = M_arr[i][j];
    
    for (vector<vector<int>>::iterator i = N.begin(); i != N.end(); i++){
        for (vector<int>::iterator j = (*i).begin(); j != (*i).end(); j++)
            cout << *j << ' ';
        cout << endl;   
    }
    
    N = zero_vector(N);
     cout << endl;
    for (vector<vector<int>>::iterator i = N.begin(); i != N.end(); i++){
        for (vector<int>::iterator j = (*i).begin(); j != (*i).end(); j++)
            cout << *j << ' ';
        cout << endl;   
    }
}
