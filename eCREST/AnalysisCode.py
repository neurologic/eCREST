def import_dsyn_with_type(syn_file,dtype_file):
    df_syn = pd.read_csv(syn_file)
    df_type = pd.read_csv(dtype_file)
    for i,r in df_syn.iterrows():
        try:
            df_syn.loc[i,'pre_type'] =df_type[df_type['id'].isin([r['pre']])].cell_type.values[0]
            df_syn.loc[i,'post_type']=df_type[df_type['id'].isin([r['post']])].cell_type.values[0]
        except:
            print(r['pre'],r['post'])
            continue
    
    df_syn.loc[:,'post_type'] = [t.lower() for t in df_syn['post_type']]
    df_syn.loc[:,'pre_type'] = [t.lower() for t in df_syn['pre_type']]

    return df_syn

def get_connect(df_syn, columns):# Get unique 'pre' and 'post' values
    '''
    columns: which columns to use for connection counts: ['pre','post'] gets connectivity by cell pairs while ['pre','post_type'] gets connectivity by pre cell - post type relationship
    '''
    df_edges = df_syn[columns].value_counts().reset_index(name='weight')

    m_cells = df_edges[columns[0]].unique()
    n_cells = df_edges[columns[1]].unique()
    
    # Create index mappings
    m_index = {cell: idx for idx, cell in enumerate(m_cells)}
    n_index = {cell: idx for idx, cell in enumerate(n_cells)}
    
    # Initialize the adjacency matrix
    matrix = np.zeros((len(m_cells), len(n_cells)))
    
    # Populate the matrix
    for _, row in df_edges.iterrows():
        i = m_index[row[columns[0]]]
        j = n_index[row[columns[1]]]
        matrix[i, j] = row['weight']

    m_labels=m_cells
    n_labels=n_cells
    return matrix, m_labels, n_labels


def plot_connect(matrix,index_,columns_):
    # Convert matrix to a DataFrame for better visualization
    matrix_df = pd.DataFrame(M, index=index_, columns=columns_) #EX: index_=pre_cells and columns_=post_cells
    
    # Display the result
    sns.heatmap(matrix_df, xticklabels=False, yticklabels=False)

def do_svd(M):
    isfull= M.shape[0] >= M.shape[1]
    S = np.linalg.svd(M, full_matrices=isfull, compute_uv=False)
    S = 100 * S / np.sum(S)
    
    return S

def do_pca(M,n_feat):
    # Apply the fraction total synapses normalization function to each row (each pre cell)

    '''
    pca_result: the data projected into PC space -- ie. scatter(pca_result[:,0],pca_result[:,1]) plots the second principle component against the 3rd to see how the data clusters or not in the space according to other features
    '''
    
    # Perform PCA
    pca_ = PCA(n_components=n_feat)  
    
    pca_result = pca_.fit_transform(M)
    
    # get loadings of dimensions onto each principal component
    loadings = pca_.components_.T

    return pca_, pca_result, loadings

def do_decomposition(df_syn,columns,norm_row,n_reps,n_feat,which_shuff,how_shuff):
    '''
    This function performs both direct svd via numpy.linalg.svd and pca (and svd) via scikit learn decomposition module. scikit pca also returns the svd result so can compare to direct svd via numpy.

    Data can be shuffled and analyzed on each iteration or just analyzed one time. If shuffled across multiple iterations, only the last model fit is returned -- the rest of the results are appended to an array and the mean and std are returned (std = [] if nreps=1)
    
    df_syn: original data in which each row is a single synapse
    columns: which columns to use for connection counts
    nreps: n_reps=1 for data or n_reps>1 for shuffle
    n_feat: number of features to analyze -- only used for pca (svd uses all columns/features)
    which_shuff: whether to shuffle 'synapses' or 'weights'
    how_shuff: only applies if which_shuff=='weights' because it changes whether whole matrix is shuffled around or if shuffles are constrained across rows
    '''
    M_, m_labels, n_labels = get_connect(df_syn, columns)
    
    S = np.zeros((n_reps, n_feat))
    E = np.zeros((n_reps, n_feat))
    E_S = np.zeros((n_reps, n_feat))
    
    for i in range(n_reps):

        if n_reps == 1:
            if norm_row==True:
                M = M_ / M_.sum(axis=1, keepdims=True)
            if norm_row==False:
                M=M_
                
        if n_reps > 1:
            
            if which_shuff=='synapses':
                '''shuffling synapses is more similar to shuffling "all" in connectivity matrix than "rows"'''
                df_syn_shuff = df_syn[columns].apply(np.random.permutation, axis=0)
                M, _, _ = get_connect(df_syn_shuff, columns)
                if norm_row==True:
                    M = M / M.sum(axis=1, keepdims=True)
    
            if which_shuff=='weights':
                # df_syn_shuff = df_syn[columns].apply(np.random.permutation, axis=0)
                # M, _, _ = get_connect(df_syn_shuff, columns)

                if how_shuff=='rows':
                    '''randomize connections across each row (so each m cell has the same number of synapses/weights, but onto different n cells)'''
                    # **NOTE that in Larry analysis, the synapses are totally shuffled across entire matrix so m cells end up with different number of synapses**
                    df = pd.DataFrame(M_)
                    df = df.apply(lambda x: np.random.permutation(x), axis=1, raw=True)
                    M = df.values

                if how_shuff=='all':
                    ''' to do the type of shuffle larry did:'''
                    i_ran = np.random.permutation(np.prod(M_.shape))
                    M = M_.flatten()[i_ran].reshape(M_.shape)
                
                if norm_row==True:
                    M = M / M.sum(axis=1, keepdims=True)
    
        scaler = StandardScaler()
        M = scaler.fit_transform(M)
    
        S_ = do_svd(M)
        S[i, :] = S_

        pca_, pca_result, loadings = do_pca(M,n_feat)
        E[i,:]= pca_.explained_variance_ratio_

        E_S_ =  pca_.singular_values_ 
        E_S[i,:]= 100 * E_S_ / np.sum(E_S_)
        
    sigS = []
    if n_reps>1:
        sigS = np.std(S, axis=0)
    S = np.mean(S, axis=0)     
    
    sigE = []
    if n_reps>1:
        sigE = np.std(E, axis=0)
    E = np.mean(E, axis=0)   

    sigE_S = []
    if n_reps>1:
        sigE_S = np.std(E_S, axis=0)
    E_S = np.mean(E_S, axis=0)   

    return m_labels, n_labels, E, sigE, E_S, sigE_S, S, sigS, pca_result, loadings