"""
Fixed Enhanced Leaderboard Rendering - Resolves HTML display issues
"""

import streamlit as st
import logging
import html # Added for escaping
from typing import Dict, Any, List
from auth.badge_manager import BadgeManager
from utils.language_utils import t, get_current_language

logger = logging.getLogger(__name__)

class ProfileLeaderboardSidebar:
    """Fixed enhanced combined profile and leaderboard sidebar component."""
    
    def __init__(self):
        self.badge_manager = BadgeManager()
    
    def render_combined_sidebar(self, user_info: Dict[str, Any], user_id: str) -> None:
        """
        Render enhanced combined user profile and leaderboard with fixed HTML rendering.
        """
        try:
            
            # Extract user data
            display_name, level, reviews_completed, score = self._extract_user_data(user_info)
            
            # Get user badges and rank
            user_badges = self.badge_manager.get_user_badges(user_id)[:4]
            user_rank_info = self.badge_manager.get_user_rank(user_id)
            leaders = self.badge_manager.get_leaderboard_with_badges(8)
            
            # Render profile section
            self._render_profile_section(display_name, level, reviews_completed, 
                                             score, user_badges, user_rank_info)
            
            # Render leaderboard section with proper error handling
            if leaders:
                self._render_leaderboard_section(leaders, user_id)
            else:
                st.info("No leaderboard data available")
                
        except Exception as e:
            logger.error(f"Error rendering enhanced sidebar: {str(e)}")

    def _extract_user_data(self, user_info: Dict[str, Any]) -> tuple:
        """Extract user data with language support."""
        current_lang = get_current_language()
        display_name = user_info.get(f"display_name_{current_lang}", 
                                   user_info.get("display_name", "User"))
        level = user_info.get(f"level_name_{current_lang}", 
                            user_info.get("level", "basic")).capitalize()
        reviews_completed = user_info.get("reviews_completed", 0)
        score = user_info.get("score", 0)
        return display_name, level, reviews_completed, score
    
    def _render_profile_section(self, display_name: str, level: str, 
                                    reviews_completed: int, score: int, 
                                    user_badges: List[Dict], user_rank_info: Dict) -> None:
        """Render profile section with fixed HTML structure."""
        
        # Get user avatar (first letter)
        avatar_letter = display_name[0].upper() if display_name else "U"
        
        # Build badge HTML safely
        badge_html = ""
        if user_badges:
            for badge in user_badges[:4]:  # Limit to 4 badges
                icon = badge.get("icon", "🏅")
                badge_name = badge.get("name", "Badge") # Assume 'name' key exists
                escaped_badge_name = html.escape(badge_name)
                badge_html += f'<span class="badge-icon-fixed" title="{escaped_badge_name}">{icon}</span>'
        else:
            badge_html = '<span class="badge-icon-fixed">🏅</span>'
        
        # Profile HTML - using smaller, safer structure
        profile_html = f'''
        <div class="sidebar-container">
            <div class="enhanced-profile-card">
                <div class="profile-header-enhanced">
                    <div class="profile-avatar">{avatar_letter}</div>
                    <div class="profile-name-enhanced">{display_name}</div>
                    <div class="profile-level-enhanced">{level}</div>
                    <div class="badge-showcase-fixed">
                        {badge_html}
                    </div>
                </div>
                <div class="stats-grid-enhanced">
                    <div class="stats-row">
                        <div class="stat-item-enhanced">
                            <div class="stat-value-enhanced">{reviews_completed}</div>
                            <div class="stat-label-enhanced">{t("review_times")}</div>
                        </div>
                        <div class="stat-item-enhanced">
                            <div class="stat-value-enhanced">{score:,}</div>
                            <div class="stat-label-enhanced">{t("score")}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
        
        # Render profile with error handling
        try:
            st.markdown(profile_html, unsafe_allow_html=True)
        except Exception as e:
            logger.error(f"Error rendering profile HTML: {str(e)}")
            # Fallback to simple display
            st.markdown(f"**{display_name}** ({level})")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Reviews", reviews_completed)
            with col2:
                st.metric("Score", f"{score:,}")
        
        # Render rank section separately
        #self._render_rank_section(user_rank_info)
    
    def _render_rank_section(self, user_rank_info: Dict) -> None:
        """Render rank section with fallback."""
        rank = user_rank_info.get("rank", 0)
        total = user_rank_info.get("total_users", 0)
        
        if rank == 0:
            return
        
        # Determine emoji and styling
        if rank == 1:
            emoji = "🥇"
        elif rank == 2:
            emoji = "🥈"
        elif rank == 3:
            emoji = "🥉"
        else:
            emoji = "🏆"
        
        rank_html = f'''
        <div class="rank-display-fixed">
            <span>{emoji}</span>
            <span>#{rank} {t('of')} {total:,} {t('users')}</span>
        </div>
        '''
        
        try:
            st.markdown(rank_html, unsafe_allow_html=True)
        except Exception as e:
            logger.error(f"Error rendering rank: {str(e)}")
            # Fallback
            st.info(f"{emoji} Rank: #{rank} of {total:,}")
    
    def _render_leaderboard_section(self, leaders: List[Dict], user_id: str) -> None:
        """
        Render leaderboard with beautiful CSS styling that actually works.
        This version carefully structures the HTML to avoid rendering issues.
        """
        
        try:
            
            # Build the leaderboard HTML in smaller, safer chunks
            header_html = f'''
            <div class="leaderboard-container-enhanced">
                <div class="leaderboard-header-enhanced">
                    🏆 {t('top_performers')}
                </div>
                <div class="leaderboard-list">
            '''
            
            # Render header first
            st.markdown(header_html, unsafe_allow_html=True)
            
            # Build items HTML safely
            items_html = ""
            for i, leader in enumerate(leaders[:6]):  # Show top 6
                rank = leader.get("rank", i + 1)
                usname = leader.get("display_name", "Unknown")[:10]  # Truncate long names
                level = leader.get("level", "basic").capitalize()
                points = leader.get("total_points", 0)
                badges = leader.get("top_badges", [])[:3]
                is_current = leader.get("uid") == user_id
                
                # Get rank display and styling
                if rank == 1:
                    rank_display = "🥇"
                    rank_class = "rank-1"
                elif rank == 2:
                    rank_display = "🥈"
                    rank_class = "rank-2"
                elif rank == 3:
                    rank_display = "🥉"
                    rank_class = "rank-3"
                else:
                    rank_display = str(rank)
                    rank_class = ""
                
                # Get badge icons
                badge_icons_html = ""
                for badge_item in badges:
                    icon = badge_item.get("icon", "🏅")
                    name = badge_item.get("name", "Badge")
                    escaped_name = html.escape(name)
                    badge_icons_html += f'<span class="badge-icon-fixed" title="{escaped_name}">{icon}</span>'
                
                # Ensure badge_icons_html is a string before escaping (it already is)
                # No, we are injecting HTML, so we don't escape badge_icons_html itself.
                # The individual names *within* it are already escaped.
                # escaped_badge_icons = html.escape(str(badge_icons_html)) # This would double-escape and show raw HTML
                # Instead, use badge_icons_html directly
                
                # Current user styling
                current_class = "current-user-enhanced" if is_current else ""
                current_indicator = '<span class="current-user-indicator-enhanced">(You)</span>' if is_current else ""
                
                # Build individual item HTML
                # Construct user_name_content carefully
                user_name_parts = [
                    html.escape(str(usname)), # Ensure name is string before escape
                    f'<span class="user-level-tag">{html.escape(str(level))}</span>' # Ensure level is string
                ]
                if current_indicator: # current_indicator is already HTML string or empty string
                    user_name_parts.append(current_indicator)
                
                user_name_content = "".join(user_name_parts)

                # Ensure badge_icons_html is a string before escaping
                # No longer needed as badge_icons_html is already constructed HTML string.

                item_html_parts = [
                    f'<div class="leaderboard-item-enhanced {current_class}">',
                    f'    <div class="rank-position-enhanced {rank_class}">{rank_display}</div>', # rank_display is emoji or str(num)
                    f'    <div class="user-info-enhanced">',
                    f'        <div class="user-name-enhanced">',
                    f'            {user_name_content}',
                    f'        </div>',
                    f'        <div class="user-badges-enhanced">{badge_icons_html}</div>', # Use the generated HTML directly
                    f'    </div>',
                    f'    <div class="user-points-enhanced">',
                    f'        <div class="points-number">{points:,}</div>', # points is an int
                    f'        <div class="points-label">{html.escape(t("points"))}</div>', # t('points') returns str
                    f'    </div>',
                    f'</div>'
                ]
                item_html = "\n".join(item_html_parts)
                items_html += item_html
            
            # Render items
            st.markdown(items_html, unsafe_allow_html=True)
            
            # Close container and add button
            footer_html = f'''
                </div>
                <button class="view-full-btn" onclick="alert('Feature coming soon!')">
                    📊 {t('view_full_leaderboard')}
                </button>
            </div>
            '''
            
            st.markdown(footer_html, unsafe_allow_html=True)
            
        except Exception as e:
            logger.error(f"Error rendering styled leaderboard: {str(e)}")
            
            
    

    