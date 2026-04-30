# Tab8：GEO 资源库（从 geo_tool.py 迁移，通过 render_tab_resources() 供主入口调用。）

import streamlit as st

from modules.resource_recommender import ResourceRecommender


def render_tab_resources(storage, brand: str) -> None:
    """渲染 Tab8：GEO 资源库。由主入口在 with tab8 内调用。"""
    st.markdown("### 📚 GEO 资源库")
    st.caption("发现 GEO 相关工具、代理、论文和社区资源，增强工具生态")

    resource_recommender = ResourceRecommender()

    # 资源统计概览
    summary = resource_recommender.get_resource_summary()
    stat_col1, stat_col2, stat_col3, stat_col4, stat_col5 = st.columns(5)
    with stat_col1:
        st.metric("总资源数", summary['total'])
    with stat_col2:
        st.metric("代理服务", summary['agents'])
    with stat_col3:
        st.metric("工具推荐", summary['tools'])
    with stat_col4:
        st.metric("论文/指南", summary['papers'])
    with stat_col5:
        st.metric("社区资源", summary['communities'])

    st.markdown("---")

    # 搜索功能
    search_col1, search_col2 = st.columns([3, 1])
    with search_col1:
        search_query = st.text_input(
            "🔍 搜索资源", 
            key="resource_search", 
            placeholder="输入关键词搜索代理、工具、论文、社区...",
            help="支持搜索资源名称、描述、功能特性等"
        )
    with search_col2:
        clear_search = st.button("清除搜索", use_container_width=True, key="clear_resource_search")
        if clear_search:
            st.session_state.resource_search = ""
            st.rerun()

    # 资源分类标签
    resource_tab1, resource_tab2, resource_tab3, resource_tab4 = st.tabs(["🤖 GEO 代理", "🛠️ 工具推荐", "📄 论文/指南", "👥 社区资源"])

    # GEO 代理
    with resource_tab1:
        st.markdown("#### 🤖 GEO 代理服务")
        st.caption("专业的 GEO 代理服务，提供高质量的内容生成和优化")

        if search_query:
            agents = resource_recommender.search_resources(search_query, "agents")
            if agents:
                st.info(f"🔍 找到 {len(agents)} 个匹配的代理服务")
        else:
            agents = resource_recommender.get_agents()

        if agents:
            for i, agent in enumerate(agents, 1):
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"##### {i}. {agent['name']} {agent.get('rating', '')}")
                    with col2:
                        if agent.get('url'):
                            st.markdown(f"[🔗 访问]({agent['url']})")

                    st.markdown(f"**{agent['description']}**")
                    st.markdown(f"**分类**：{agent.get('category', 'N/A')}")

                    if agent.get('features'):
                        st.markdown("**功能特性**：")
                        features_text = " | ".join([f"✓ {f}" for f in agent['features']])
                        st.markdown(features_text)

                    if agent.get('url'):
                        st.markdown(f"**链接**：{agent['url']}")
        else:
            st.info("💡 暂无匹配的代理资源。尝试使用其他关键词搜索。")

    # 工具推荐
    with resource_tab2:
        st.markdown("#### 🛠️ 工具推荐")
        st.caption("GEO 相关的工具和服务，帮助优化内容效果")

        if search_query:
            tools = resource_recommender.search_resources(search_query, "tools")
            if tools:
                st.info(f"🔍 找到 {len(tools)} 个匹配的工具")
        else:
            tools = resource_recommender.get_tools()

        if tools:
            # 按分类分组显示
            categories = {}
            for tool in tools:
                cat = tool.get('category', '其他')
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(tool)

            for category, category_tools in categories.items():
                st.markdown(f"##### 📁 {category}")
                for i, tool in enumerate(category_tools, 1):
                    with st.container(border=True):
                        col1, col2 = st.columns([3, 1])
                        with col1:
                            st.markdown(f"**{tool['name']}** {tool.get('rating', '')}")
                        with col2:
                            if tool.get('url'):
                                st.markdown(f"[🔗 访问]({tool['url']})")

                        st.markdown(f"*{tool['description']}*")

                        if tool.get('features'):
                            st.markdown("**功能**：")
                            features_text = " | ".join([f"✓ {f}" for f in tool['features']])
                            st.markdown(features_text)

                        if tool.get('url'):
                            st.markdown(f"**链接**：{tool['url']}")
        else:
            st.info("💡 暂无匹配的工具资源。尝试使用其他关键词搜索。")

    # 论文/指南
    with resource_tab3:
        st.markdown("#### 📄 论文/指南")
        st.caption("GEO 相关的论文、指南、文档，深入学习 GEO 策略")

        if search_query:
            papers = resource_recommender.search_resources(search_query, "papers")
            if papers:
                st.info(f"🔍 找到 {len(papers)} 个匹配的论文/指南")
        else:
            papers = resource_recommender.get_papers()

        if papers:
            # 按重要性排序
            importance_order = {"高": 3, "中": 2, "低": 1}
            papers_sorted = sorted(papers, key=lambda x: importance_order.get(x.get('importance', '低'), 1), reverse=True)

            # 按重要性分组显示
            high_importance = [p for p in papers_sorted if p.get('importance') == '高']
            medium_importance = [p for p in papers_sorted if p.get('importance') == '中']
            low_importance = [p for p in papers_sorted if p.get('importance') == '低']

            if high_importance:
                st.markdown("##### 🔥 高重要性（必读）")
                for paper in high_importance:
                    with st.container(border=True):
                        st.markdown(f"**🔥 {paper['title']}**")
                        st.markdown(f"*{paper['description']}*")
                        st.markdown(f"**分类**：{paper.get('category', 'N/A')} | **日期**：{paper.get('date', 'N/A')}")
                        if paper.get('url'):
                            st.markdown(f"🔗 [{paper['url']}]({paper['url']})")

            if medium_importance:
                st.markdown("##### ⭐ 中重要性（推荐阅读）")
                for paper in medium_importance:
                    with st.container(border=True):
                        st.markdown(f"**⭐ {paper['title']}**")
                        st.markdown(f"*{paper['description']}*")
                        st.markdown(f"**分类**：{paper.get('category', 'N/A')} | **日期**：{paper.get('date', 'N/A')}")
                        if paper.get('url'):
                            st.markdown(f"🔗 [{paper['url']}]({paper['url']})")

            if low_importance:
                st.markdown("##### 📌 低重要性（参考阅读）")
                for paper in low_importance:
                    with st.container(border=True):
                        st.markdown(f"**📌 {paper['title']}**")
                        st.markdown(f"*{paper['description']}*")
                        st.markdown(f"**分类**：{paper.get('category', 'N/A')} | **日期**：{paper.get('date', 'N/A')}")
                        if paper.get('url'):
                            st.markdown(f"🔗 [{paper['url']}]({paper['url']})")
        else:
            st.info("💡 暂无匹配的论文/指南资源。尝试使用其他关键词搜索。")

    # 社区资源
    with resource_tab4:
        st.markdown("#### 👥 社区资源")
        st.caption("GEO 相关的社区和论坛，与其他用户交流经验")

        if search_query:
            communities = resource_recommender.search_resources(search_query, "communities")
            if communities:
                st.info(f"🔍 找到 {len(communities)} 个匹配的社区")
        else:
            communities = resource_recommender.get_communities()

        if communities:
            for i, community in enumerate(communities, 1):
                with st.container(border=True):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"##### {i}. {community['name']} {community.get('rating', '')}")
                    with col2:
                        if community.get('url'):
                            st.markdown(f"[🔗 访问]({community['url']})")

                    st.markdown(f"*{community['description']}*")
                    st.markdown(f"**分类**：{community.get('category', 'N/A')}")

                    if community.get('url'):
                        st.markdown(f"**链接**：{community['url']}")
        else:
            st.info("💡 暂无匹配的社区资源。尝试使用其他关键词搜索。")

    # 搜索结果显示（跨分类）
    if search_query:
        all_results = resource_recommender.search_resources(search_query)
        if all_results:
            st.markdown("---")
            st.markdown("#### 🔍 搜索结果汇总")
            st.info(f"共找到 {len(all_results)} 个匹配资源（跨所有分类）")

            # 按类型分组显示
            results_by_type = {}
            for result in all_results:
                res_type = result.get('type', 'unknown')
                if res_type not in results_by_type:
                    results_by_type[res_type] = []
                results_by_type[res_type].append(result)

            type_names = {
                'agent': '🤖 代理服务',
                'tool': '🛠️ 工具',
                'paper': '📄 论文/指南',
                'community': '👥 社区'
            }

            for res_type, results in results_by_type.items():
                if results:
                    st.markdown(f"##### {type_names.get(res_type, res_type)} ({len(results)} 个)")
                    for result in results:
                        with st.container(border=True):
                            name_key = 'name' if 'name' in result else 'title'
                            st.markdown(f"**{result.get(name_key, 'N/A')}**")
                            st.caption(result.get('description', ''))
                            if result.get('url'):
                                st.markdown(f"🔗 [{result['url']}]({result['url']})")

    # =======================
