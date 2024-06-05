import './BlockDropdown.scss'
import {useState} from "react";

export const BlockDropdown = ({children}) => {

    const [folded, setFolded] = useState(true)
    return (
        <div className='block__dropdown'>
            {children}
            <button onClick={() => setFolded(!folded)} className="dropdown__fold-btn">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="12" transform="rotate(180 12 12)" fill="#FFCB00"/>
                    <path d="M15.4828 13.4964C15.7617 13.7748 16.2133 13.7749 16.4924 13.4966C16.7726 13.2174 16.7727 12.7637 16.4927 12.4843L12.7064 8.70512C12.3161 8.31548 11.6839 8.31548 11.2936 8.70512L7.50726 12.4843C7.22731 12.7637 7.22745 13.2174 7.50757 13.4966C7.78666 13.7749 8.23826 13.7748 8.51725 13.4964L12 10.0219L15.4828 13.4964Z" fill="black"/>
                </svg>
            </button>
        </div>
    );
};