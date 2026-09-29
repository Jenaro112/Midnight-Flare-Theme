import React, { useState, useEffect } from "react";
import "./example.css";

interface ButtonProps {
    label: string;
    onClick: () => void;
    disabled?: boolean;
}

const CustomButton: React.FC<ButtonProps> = ({
    label,
    onClick,
    disabled = false,
}) => {
    const [isHovered, setIsHovered] = useState(false);

    useEffect(() => {
        console.log("Button mounted");
    }, []);

    return (
        <button
            className={`btn ${isHovered ? "hover" : ""}`}
            onClick={onClick}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            disabled={disabled}
        >
            {label}
        </button>
    );
};

export default CustomButton;
