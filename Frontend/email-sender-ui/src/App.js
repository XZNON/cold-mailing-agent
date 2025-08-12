import React, { useState, useEffect } from 'react';
import './App.css';

// --- Game Constants ---
const HOLE_COUNT = 9; // The number of holes in our game (3x3 grid)
const MOLE_UP_DURATION = 850; // How long a mole stays visible in milliseconds

function App() {
    // --- Existing State ---
    const [jobRole, setJobRole] = useState('');
    const [recipientsFile, setRecipientsFile] = useState(null);
    const [resumeFile, setResumeFile] = useState(null);
    const [message, setMessage] = useState('');
    const [messageType, setMessageType] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    // --- New State for Whack-a-Mole Game ---
    const [moles, setMoles] = useState(new Array(HOLE_COUNT).fill(false)); // An array to track which holes have a mole
    const [score, setScore] = useState(0);

    // --- Game Loop Logic ---
    useEffect(() => {
        // We only want the game loop to run when we are in the loading state.
        if (!isLoading) {
            return;
        }

        // This timer will randomly pop up a mole in a different hole.
        const gameInterval = setInterval(() => {
            const randomIndex = Math.floor(Math.random() * HOLE_COUNT);
            
            // Show the mole
            setMoles(currentMoles => {
                const newMoles = [...currentMoles];
                newMoles[randomIndex] = true;
                return newMoles;
            });

            // After a short duration, hide the mole again.
            setTimeout(() => {
                setMoles(currentMoles => {
                    const newMoles = [...currentMoles];
                    newMoles[randomIndex] = false;
                    return newMoles;
                });
            }, MOLE_UP_DURATION);

        }, 1000); // A new mole attempts to pop up every second

        // Cleanup function to stop the game loop when loading is finished.
        return () => {
            clearInterval(gameInterval);
        };
    }, [isLoading]);


    const handleWhack = (index) => {
        // Only score if a mole is actually present
        if (!moles[index]) {
            return;
        }
        
        setScore(prevScore => prevScore + 1);
        
        // Hide the mole immediately after it's whacked
        setMoles(currentMoles => {
            const newMoles = [...currentMoles];
            newMoles[index] = false;
            return newMoles;
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        if (!jobRole || !recipientsFile || !resumeFile) {
            setMessage('Please fill out all fields and select both files.');
            setMessageType('error');
            return;
        }

        const formData = new FormData();
        formData.append('job_role', jobRole);
        formData.append('file', recipientsFile);
        formData.append('resume', resumeFile);

        // Prepare for loading and start the game
        setIsLoading(true);
        setScore(0); // Reset score for the new game
        setMessage('');
        setMessageType('');

        try {
            const endpoint = 'http://127.0.0.1:8000/send_mail';
            const response = await fetch(endpoint, {
                method: 'POST',
                body: formData,
            });

            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.detail || `Server error: ${response.statusText}`);
            }
            
            setMessage(result.Message);
            setMessageType('success');
            event.target.reset();

        } catch (error) {
            setMessage(`An error occurred: ${error.message}`);
            setMessageType('error');
        } finally {
            // Stop the loading state and the game
            setIsLoading(false);
        }
    };

    return (
        <div className="App">
            <div className="container">
                <h1>Send Job Applications</h1>
                
                {isLoading ? (
                    // --- The Whack-a-Mole Game UI ---
                    <div className="minigame-container">
                        <h3>Sending Emails... Whack a mole!</h3>
                        <p className="score-display">Score: {score}</p>
                        <div className="whack-a-mole-grid">
                            {moles.map((isMoleVisible, index) => (
                                <div key={index} className="hole">
                                    {isMoleVisible && (
                                        <div className="mole" onClick={() => handleWhack(index)}>
                                            🐹
                                        </div>
                                    )}
                                </div>
                            ))}
                        </div>
                    </div>
                ) : (
                    // --- The Form UI ---
                    <form onSubmit={handleSubmit}>
                        {/* Form groups remain the same */}
                        <div className="form-group">
                            <label htmlFor="jobRole">Job Role</label>
                            <input type="text" id="jobRole" placeholder="e.g., Software Engineer" onChange={e => setJobRole(e.target.value)} required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="recipientsFile">Recipients File (Excel)</label>
                            <input type="file" id="recipientsFile" accept=".xlsx, .xls, .csv" onChange={e => setRecipientsFile(e.target.files[0])} required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="resumeFile">Your Resume</label>
                            <input type="file" id="resumeFile" accept=".pdf,.doc,.docx" onChange={e => setResumeFile(e.target.files[0])} required />
                        </div>
                        <button type="submit" disabled={isLoading}>Send Emails</button>
                    </form>
                )}

                {/* --- Feedback Message Area --- */}
                {message && (
                    <p id="message" className={messageType}>
                        {message}
                        {messageType === 'success' && <span className="final-score"> Final Score: {score}!</span>}
                    </p>
                )}
            </div>
        </div>
    );
}

export default App;