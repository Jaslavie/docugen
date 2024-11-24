import React, { createContext, useState } from "react";

// Define the context type
interface MemoryContextType {
    memories: string[];
    addMemory: (memory: string) => void; 
    removeMemory: (memory: string) => void;
}

// Create the context
const MemoryContext = createContext<MemoryContextType | undefined>(undefined);

// Create a custom hook to use the context
export const MemoryProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [memories, setMemories] = useState<string[]>([
        "The UCI Design-a-thon is a 24-hour event that takes place on the UCI campus. It is a competition that challenges college students to come up with innovative solutions to real-world problems through design.",
        "The Design-a-thon is structured similarly to a hackathon: https://mlh.io/"
    ]);

    // initialize function to add new memories to the context
    const addMemory = (memory: string) => {
        setMemories([...memories, memory]);
    };

    // initialize function to remove memories from the context
    const removeMemory = (memory: string) => {
        setMemories(memories.filter((m) => m !== memory)); // filter out the memory to remove
    };

    // return the context provider for use
    return (
        <MemoryContext.Provider value={{ memories, addMemory, removeMemory }}>
            {children} {/* pass down the context to the children */}
        </MemoryContext.Provider>
    )
}