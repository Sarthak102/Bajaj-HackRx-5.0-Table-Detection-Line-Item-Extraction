import React, { useState } from "react";
import axios from "axios";

function Home() {
    const [file, setFile] = useState(null);
    const [result, setResult] = useState("");

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleSubmit = async () => {
        const formData = new FormData();
        formData.append("file", file);

        const response = await axios.post("/upload-invoice/", formData);
        setResult(response.data.processed_text);
    };

    return (
        <div>
            <h1>Upload Invoice</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleSubmit}>Submit</button>
            <div>{result}</div>
        </div>
    );
}

export default Home;
