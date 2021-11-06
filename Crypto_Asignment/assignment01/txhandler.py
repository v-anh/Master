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
        usedUTOX = []
        for trans_input in tx.numInputs():
            output_index = trans_input.prevTxHash
            pre_hash = trans_input.signatures
            utxo_verify = utxo.UTXO(pre_hash, output_index)
            
            if not self.__pool.contains(utxo_verify):
                return False
                
            if not Crypto.verifySignature(tx.getOutput(), tx.getRawDataToSign(output_index), signature):
                return False
                
            if usedUTOX.__contains___(utxo_verify):
                return False
        return True


    """
    Handles each epoch by receiving an unordered array of proposed transactions, checking each
    transaction for correctness, returning a mutually valid array of accepted transactions, and
    updating the current UTXO pool as appropriate.
    """
    def handleTxs(self, txs):
        # IMPLEMENT THIS
        return 
