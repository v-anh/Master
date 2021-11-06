from utxo import UTXOPool
from transaction import Transaction

class TxHandler:
    """
    Creates a public ledger whose current UTXOPool (collection of unspent transaction outputs) is {@code pool}.
    """
    
    def __init__(self, pool: UTXOPool):
        # IMPLEMENT THIS
        self.utxoPool = UTXOPool(pool)
        return
    """
    @return true if:
    (1) all outputs claimed by {@code tx} are in the current UTXO pool, 
    (2) the signatures on each input of {@code tx} are valid, 
    (3) no UTXO is claimed multiple times by {@code tx},
    (4) all of {@code tx}s output values are non-negative, and
    (5) the sum of {@code tx}s input values is greater than or equal to the sum of its output
        values; and false otherwise.
    """
    def isValidTx(self, tx: Transaction) -> bool:
        # IMPLEMENT THIS
        utxoSet = UTXOPool()
        pSum = 0
        sum = 0
        for trans_input in tx.numInputs():
            output_index = trans_input.prevTxHash
            pre_hash = trans_input.signatures
            utxo_verify = utxoPool.UTXO(pre_hash, output_index)
            
            if !utxoPool.contains(utxo_verify) || Crypto.verifySignature(tx.getOutput()), tx.getRawDataToSign(output_index), signature) || utxoSet.contains(utxo_verify):
                return False
            
            utxoSet.addUTXO(utxo_verify, output)
            pSum += output.values
        for trans_output in tx.getOutput:
            if trans_output.value < 0:
                return False
            sum += output.value
        
        if pSum < sum:
            return False
        return True


    """
    Handles each epoch by receiving an unordered array of proposed transactions, checking each
    transaction for correctness, returning a mutually valid array of accepted transactions, and
    updating the current UTXO pool as appropriate.
    """
    def handleTxs(self, possibleTxs):
        acceptedTx = []
        i = 0
        while i < len(possibleTxs):
            tx = possibleTxs[i]
            if self.isValidTx(tx):
                acceptedTx.append(tx)

                self.__removeConsumedCoinsFromPool(tx)
                self.__addCreatedCoinsToPool(tx)
            i += 1

        result = [None for _ in range(len(acceptedTx))]
        acceptedTx.toArray(result)
        return result

    def __addCreatedCoinsToPool(self, tx):
        outputs = tx.getOutputs()
        j = 0
        while j < len(outputs):
            output = outputs[j]
            utxo = UTXO(tx.getHash(), j)
            self.utxoPool.addUTXO(utxo, output)
            j += 1

    def __removeConsumedCoinsFromPool(self, tx):
        inputs = tx.getInputs()
        j = 0
        while j < len(inputs):
            input = inputs[j]
            utxo = UTXO(input.prevTxHash, input.outputIndex)
            self.utxoPool.removeUTXO(utxo)
            j += 1
