import React, { useState } from 'react'

export default function Clicker() {

    const [count, setCount] = useState(0)

    const addOne = () => setCount(count + 1)
    const subOne = () => setCount(count - 1)

    return (
        <>
            <div style={{display: 'flex', justifyContent: 'space-evenly', backgroundColor: 'lightgrey'}}>
                <button onClick={addOne} style={{marginLeft: '10px', backgroundColor: 'lightblue', padding: '10px', border: 'none', borderRadius: '4px'}}>
                    Click Me to increase!
                </button>
                <p> Count: {count} </p>
                <button onClick={subOne} style={{marginLeft: '10px', backgroundColor: 'lightblue', padding: '10px', border: 'none', borderRadius: '4px'}}>
                    Click me to decrease!
                </button>
            </div>
        </>
    )
}
