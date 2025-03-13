from hfc.fabric import Client
import json
import logging

logging.basicConfig(level=logging.INFO, filename='blockchain/blockchain.log')

cli = Client(net_profile="blockchain/fabric_network/network.json")

def log_to_blockchain(query: str, response: str):
    """Log a query and response to the blockchain."""
    try:
        org1_admin = cli.get_user(org_name='Org1', name='Admin')
        response = cli.chaincode_invoke(
            requestor=org1_admin,
            channel_name='mychannel',
            peers=['peer0.org1.example.com'],
            chaincode_name='log',
            fcn='LogQuery',
            args=[query, response],
        )
        logging.info(f"Logged to blockchain: {query}")
        return response
    except Exception as e:
        logging.error(f"Blockchain logging failed: {e}")
        return None

if __name__ == "__main__":
    log_to_blockchain("Test query", "Test response")