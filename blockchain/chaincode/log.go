package main

import (
    "fmt"
    "github.com/hyperledger/fabric-contract-api-go/contractapi"
)

type LogChaincode struct {
    contractapi.Contract
}

func (c *LogChaincode) LogQuery(ctx contractapi.TransactionContextInterface, query string, response string) error {
    logData := fmt.Sprintf("Query: %s, Response: %s", query, response)
    return ctx.GetStub().PutState(query, []byte(logData))
}

func (c *LogChaincode) GetQuery(ctx contractapi.TransactionContextInterface, query string) (string, error) {
    data, err := ctx.GetStub().GetState(query)
    if err != nil {
        return "", err
    }
    if data == nil {
        return "", fmt.Errorf("Query %s not found", query)
    }
    return string(data), nil
}

func main() {
    chaincode, err := contractapi.NewChaincode(new(LogChaincode))
    if err != nil {
        fmt.Printf("Error creating chaincode: %s", err)
        return
    }
    if err := chaincode.Start(); err != nil {
        fmt.Printf("Error starting chaincode: %s", err)
    }
}