class Collection < ApplicationRecord
  has_many :skins, before_add: :get_category

  private

  def get_category(skin)
    update(category: skin.category)
  end
end
