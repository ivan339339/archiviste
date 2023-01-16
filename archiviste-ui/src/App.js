import React, { useState, useEffect } from 'react'

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  })

  return (
      <div>
        {(typeof data.datasets === 'undefined') ? (
          <p>Loading...</p>
        ) : (
          data.datasets.map((datasetObj, index) => {
            return (
              [
              <h3 key={datasetObj.name}>name: {datasetObj.name}</h3>,
              <p  key={datasetObj.description}> desc: {datasetObj.description}</p>,
              <p  key={datasetObj.owner}> owner: {datasetObj.owner}</p>
              ]
            )
          }))}
      </div>
  )
}

export default App